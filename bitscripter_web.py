import json # Yes, we're using this instead of a DB. I know.
import itty3 # Should be installed already, as indicated by requirements.txt, https://itty3.readthedocs.io
import bitscripter # This is how we'll reference the functions of the main scripting logic, such as it is
import os # This is to show filenames and shit like that.

bsapp = itty3.App() # Object creation function for itty3

url_prefix = '/bitscripter' # In case we have to share our server
url_prefix_alertify = '/alertify' # Michael adding alertify randomly

@bsapp.get(url_prefix_alertify + '/')
def index_alertify(request):
    with open('alertify_index.html') as alertify_index_file:
        template = alertify_index_file.read()
    return bsapp.render(request, template)

@bsapp.get(url_prefix + '/')
def index(request):
    '''Handles the '/' route for the bitscripter'''

    with open('bitscripter_index.html') as index_file:
        template = index_file.read()

    with open('bitscripter_data.json') as data_file:
        data = json.load(data_file)


    script_content = ''

    # Make the list that we'll be pushing in later and replacing
    # {{ content }} with.
    for offset, item in enumerate(data.get("scripts", [])):
        script_content += '<li>{}</li>'.format(item)

    if not script_content:
        script_content = '<li>Nothing to do!</li>'

    # Find and replace "{{ content }}" in the HTML with our new update
    template = template.replace('{{ script_content }}', script_content)

    ##### Add Results #####
    results_content = ''

    # Make the list that we'll be pushing in later and replacing
    # {{ content }} with.
    for offset, item in enumerate(data.get("results", [])):
        results_content += '<li>{}</li>'.format(item)

    if not results_content:
        results_content = '<li>Nothing to do!</li>'

    # Find and replace "{{ content }}" in the HTML with our new update
    template = template.replace('{{ bitscripter_results_content }}', results_content)
    ##### Added Results #####


    # Build and render an HttpResponse object including our content
    # and various boilerplate things like headers
    return bsapp.render(request, template)

@bsapp.post(url_prefix + '/runscript/')
def append_script(request):
    '''Update a table of scripts as entered.

    You can invoke it by adding web links to an HTML page
    that refer to /update_cmd/.
    '''
    with open("bitscripter_data.json") as data_file:
        data = json.load(data_file)

    new_script = request.POST.get('runscript', '---').strip()


    data['scripts'].append(new_script)

    with open("bitscripter_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    # Run the script
    LOGGER.info("Script is as follows: " + str(new_script))
    new_script_result = str(bitscripter.stackit(new_script))

    # Add the script result
    data['results'].append(new_script_result)
    with open("bitscripter_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    return bsapp.redirect(request, url_prefix + '/')


# This just makes sure that we can still import this as
# a library or run it standalone.
if __name__ == "__main__":

    # -------- Logging Setup -------- #
    # We're going to use the logger from
    # the bsapp object, which it has because
    # the itty3 class creates a logger upon
    # instantiation.
    LOGGER = bsapp.get_log()
    LOGGER.setLevel('INFO')
    LOGGER.info(os.path.basename(__file__))
    # -------- End Logging Setup ---- #

    # This runs the app. This won't be run if
    # web_app gets imported.
    bsapp.run(addr="0.0.0.0",
        port=8000,
        debug=None,
        static_url_path=None,
        static_root=None
    )
