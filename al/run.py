from app import al


@al.route('/')
def hello_world():
    return 'hell world'


if __name__ == "__main__":
    al.run("0.0.0.0", threaded=True, port="7777")
