sudo mkdir -p /mongodata
#this is to make a new directory to which we will mount the database volume to persist data

#sudo docker run -d -v mongodata:/data/db --name mongodb -d mongo:4.4.6
sudo docker run -it -v mongodata:/data/db -p 27017:27017 --name mongodb -d mongo:4.4.6
#installed a dockerized mongodb with mounted volume on the host. Replace the path in app.py with your real database for prod

echo "started a Mongo DB on port 27017"