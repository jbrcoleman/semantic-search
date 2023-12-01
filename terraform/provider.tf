terraform {
  backend "gcs" {
    bucket = "terraform-state-gcp-project-1478"
    prefix = "terraform/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0"
      
    }
  }
}

provider "google" {
  project = "gothic-welder-398814"
  region  = "us-central1"
}
