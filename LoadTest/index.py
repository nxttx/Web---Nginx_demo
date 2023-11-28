import flask 
import os
# import threading for multi-threading
import threading
import urllib.request

# create threadpool
threadpool = []

amount1 = 0
amount2 = 0

app = flask.Flask(__name__)

@app.route('/')
def index():
    global amount1, amount2
    # clear the threadpool
    threadpool.clear()
    # reset the amount of requests
    amount1 = 0
    amount2 = 0

    for i in range(1000):
        # create a thread
        thread = threading.Thread(target=check)
        # start the thread
        thread.start()
        # add the thread to the threadpool
        threadpool.append(thread)
    # wait for all threads to finish
    for thread in threadpool:
        thread.join()
    # return the result
    return "Amount of requests to server 1: " + str(amount1) + "<br>Amount of requests to server 2: " + str(amount2)


def check():
    global amount1, amount2
    response = urllib.request.urlopen("http://nginx/api/check").read().decode("utf-8")
    # check the response
    if response == "1":
        amount1 += 1
    elif response == "2":
        amount2 += 1

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))

    from waitress import serve
    serve(app, host='0.0.0.0', port=port)
    

