import pickle

# Đọc kết quả clustering từ file 'api_clusters.pkl'
with open('api_clusters.pkl', 'rb') as f:
    clusters = pickle.load(f)

# Số lượng clusters
n_cluster = len(clusters)

# In số lượng clusters
print(f"Số lượng clusters: {n_cluster}")

# Ví dụ: In danh sách các API trong cluster 0
print("\nDanh sách các API trong cluster 0:")
for api in clusters[0]:
    print(f" - {api}")
    
for cluster_id, api_list in clusters.items():
    print(f"\nCluster {cluster_id}:")
    for api in api_list:
        print(f" - {api}")