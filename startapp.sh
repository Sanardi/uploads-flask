
sudo docker stop myapp && sudo docker rm myapp 
#this stops any existing instances and removes old images


echo "......."

echo "I will start the docker app now"

docker build --no-cache -t myappimage:latest .


#Run the Docker container using the command shown below.


docker run --name myapp -p 5000:5000 myappimage


echo The application will be accessible at http:127.0.0.1:5000
