
def before_all(context):
    context.headers = {}
    #context.json_responses = json_responses


def after_feature(context, feature):
    context.headers.clear()
