import json
import zipfile


def get_endpoint(endpoint, name, status, gender):
    if name:
        endpoint += f"name={name}"
    if status:
        endpoint += f"status={status}" if endpoint[-1] == "?" else f"&status={status}"
    if gender:
        endpoint += f"gender={gender}" if endpoint[-1] == "?" else f"&gender={gender}"
    return endpoint


def create_json_file(json_response):
    file_path = "tmp/json_response.json"
    with open(file_path, "w") as json_file:
        json.dump(json_response, json_file)
    return file_path


def create_zip(json_response):
    out_zip_file = "tmp/response.zip"
    file_to_write = create_json_file(json_response)
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(out_zip_file, mode="w")
    try:
        zf.write(file_to_write, file_to_write, compress_type=compression)
    except FileNotFoundError as e:
        print(f" *** Exception occurred during zip process - {e}")
    finally:
        zf.close()
        return out_zip_file
