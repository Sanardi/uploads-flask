

echo "I will start the docker app now"

docker build --no-cache -t upload-flask-app:latest .


#Run the Docker container using the command shown below.


docker run --name upload -d -p 5000:5000 upload-flask-app


echo The application will be accessible at http:127.0.0.1:5000
