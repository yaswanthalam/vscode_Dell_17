import speedtest
st = speedtest.Speedtest()
download = st.download() / 1_000_000
upload = st.upload() / 1_000_000
ping = st.results.ping
print(f"Download Speed: {download:.2f} Mbps")
print(f"Upload Speed: {upload:.2f} Mbps")
print(f"Ping : {ping:.2f} ms")