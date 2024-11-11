import open3d as o3d

# PLYファイルを読み込み
ply_file = "/home/ryusei22/maps/glim_slam.ply"  # 変換したいPLYファイルのパスを指定
pcd_file = "/home/ryusei22/maps/glim_slam.pcd"  # 出力するPCDファイルのパスを指定

# PLYファイルをPointCloudとして読み込む
point_cloud = o3d.io.read_point_cloud(ply_file)

# 読み込んだPointCloudをPCD形式で保存
o3d.io.write_point_cloud(pcd_file, point_cloud)

print(f"{ply_file} を {pcd_file} に変換しました。")
