import json
import os
import re
from jsonpath import jsonpath
from urllib.parse import urlparse

from airflow.exceptions import AirflowException
from airflow.models import Variable
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.plugins_manager import AirflowPlugin

from smartflow.utils.constants import REGION_ID_REGEX


def _s3_get_file(s3_loc, local_path=None, aws_conn_id="smartflow_aws_conn"):
    _local_path = local_path
    if local_path is None:
        airflow_home = os.environ.get("AIRFLOW_HOME")
        _local_path = f"{airflow_home}/dags/data/region"
    if type(s3_loc) is tuple:
        bucket, key = s3_loc
    else:
        parsed_url = urlparse(s3_loc)
        bucket, key = (parsed_url.netloc, parsed_url.path.lstrip("/"))
    s3 = AwsBaseHook(aws_conn_id=aws_conn_id, client_type="s3").get_client_type(client_type="s3")
    s3.download_file(bucket, key, _local_path)
    return _local_path


def get_json_attr(json_loc, json_path, aws_conn_id="smartflow_aws_conn"):
    """
    get_json_attr

    Retrieves an attribute at a given json_path from the json file at the given local path or S3 location.
    """
    if type(json_loc) is tuple or json_loc.startswith("s3://"):
        _local_path = _s3_get_file(json_loc, aws_conn_id)
    else:
        _local_path = json_loc
    with open(_local_path) as geojson_file:
        geojson = json.load(geojson_file)
    value = jsonpath(geojson, json_path)[0]
    if value is False:
        raise AirflowException(f"{json_path} was not found in the json file at {json_loc}")
    return value


def smart_imagery_s3():
    #return Variable.get("smart_imagery_s3", default_var="s3://smart-imagery")
    #return Variable.get("smart_imagery_s3", default_var="s3://eccoe-scratch")
    return "s3://eccoe-scratch"


def smart_imagery_annotations_s3():
    return Variable.get("smart_imagery_annotations_s3", default_var=f"{smart_imagery_s3()}/annotations")


def smart_region_aoi(region_id):
    if not re.match(REGION_ID_REGEX, region_id):
        raise AirflowException(f"{region_id} is not a valid region id")
    return get_json_attr(
        f"{smart_imagery_annotations_s3()}/region_models/{region_id}.geojson", "$.features[0].geometry"
    )


class SmartflowPlugin(AirflowPlugin):
    name = "smartflow"
    macros = [get_json_attr, smart_imagery_s3, smart_imagery_annotations_s3, smart_region_aoi]
