gcloud app deploy
Services to deploy:

descriptor:                  [/Users/jpuyy/git/gcp-infrastructure/appengine/service-a/app.yaml]
source:                      [/Users/jpuyy/git/gcp-infrastructure/appengine/service-a]
target project:              [gcp-architect-364916]
target service:              [default]
target version:              [20221119t191423]
target url:                  [https://gcp-architect-364916.df.r.appspot.com]
target service account:      [App Engine default service account]


Do you want to continue (Y/n)?  Y

Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 0 files to Google Cloud Storage                ═╣
╚════════════════════════════════════════════════════════════╝
File upload done.
Updating service [default]...done.                                                                                                                                                          
Setting traffic split for service [default]...done.                                                                                                                                         
Deployed service [default] to [https://gcp-architect-364916.df.r.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse
