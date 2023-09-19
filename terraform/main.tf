provider "google" {
  credentials = file("./credentials.json")  //Get your gcp credentials
  project     = "YOUR_PROJECT_ID" //It needs to be changed to the gcp project id
  region      = "us-central1" // region to be changed to gcp service
}

resource "google_cloud_run_service" "my_service" {
  name     = "tkzhu_flask_web"
  location = "us-central1" 

  template {
    spec {
      containers {
        image = "tkzhu66/tkzhu-web-app:latest"
      }
    }
  }
}
