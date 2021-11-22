def cluster_client():
    return ClusterClient(
        cluster_name="my-cluster",
        datacenter_name="dc9",
        port=9042,
        ssl_cert=DUMMY_CERT,
        username="the_user",
        password="fake",
    )
t = ClusterClient()
print(t)