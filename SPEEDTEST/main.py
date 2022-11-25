

# SKUYMI [helmisalsabila.com]

import speedtest as s 

st = s.Speedtest()

download = st.download()
upload = st.upload()

print('Download: ', download,'Mbps')
print('Upload: ', upload,'Mbps')