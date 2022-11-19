$ gcloud app deploy
```
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
```

$ gcloud app deploy --version=v1-1-1

$ gcloud app versions list

```
$ gcloud app services set-traffic default --splits=v1-1-1=.5,v1-1-2=.5
Setting the following traffic allocation:
 - gcp-architect-364916/default/v1-1-1: 0.5
 - gcp-architect-364916/default/v1-1-2: 0.5
NOTE: Splitting traffic by ip.
Any other versions of the specified service will receive zero traffic.
Do you want to continue (Y/n)?  Y

Setting traffic split for service [default]...done.

$ gcloud app services set-traffic default --splits=v1-1-1=.5,v1-1-2=.5 --help


     --split-by=SPLIT_BY; default="ip"
        Whether to split traffic based on cookie, IP address or random.
        SPLIT_BY must be one of: cookie, ip, random.

$ gcloud app services set-traffic default --splits=v1-1-1=.5,v1-1-2=.5 --split-by=random

$ watch curl -s https://gcp-architect-364916.df.r.appspot.com
```