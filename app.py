from returnData import app

from subprocess import call
data = call("sudo apt-get install xvfb", shell=True)
print(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)