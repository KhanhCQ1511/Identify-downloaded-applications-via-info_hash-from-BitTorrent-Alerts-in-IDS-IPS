# Identify downloaded applications via info_hash from BitTorrent Alerts in IDS/IPS

## Introduction
BitTorrent is a peer-to-peer (P2P) file sharing protocol used to distribute data over a network, without going through an intermediary server. Instead of downloading entire files from a single source, the BitTorrent protocol allows downloading small pieces of files from many different users at the same time. In particular, this protocol is exploited by hackers to transmit secret data. It's the reason why IDS/IPS systems often generate warnings when detecting actions related to Torrent.


## So are you curious what users have downloaded via Bittorent using only IDS/IPS?
Alerts often appear on IDS/IPS related to P2P Bittorent:
- ET P2P BitTorrent DHT ping request
- ET P2P BitTorrent DHT announce_peers request
- ET P2P Bittorrent P2P Client User-Agent (uTorrent)
- ET P2P BitTorrent peer sync
- ET P2P BitTorrent - Torrent File Downloaded
- ET P2P Possible Torrent Download via HTTP Request

After I saw the warnings about Bittorent users I wondered what they were using it to download from here. I tried to find out a payload of one of these alerts
![image](https://github.com/user-attachments/assets/9387393d-2e64-4850-917b-3146d2be32f1)
Based on the information I just decoded, I discovered that the user was uploading a file to Bittorent and had the info_hash as above. However, I still couldn't decode this hash until I read a post below: <a href="https://stackoverflow.com/questions/5637268/how-do-you-decode-info-hash-information-from-tracker-announce-request" target="_blank">Link</a>. It explains pretty well how to decode this hash to SHA1. I have followed it in the python code I provided.
</br>However, I had trouble figuring out the hash of the packaged file. I continued to research and analyze and found a github that allowed me to create a torrent link from this hash: https://hardrisk.github.io/magnet/
</br>=> From here I get the link, use Bittorrent Client to open. I will get the application I need to know.

## Detail steps
Download the file, execute it and enter the resulting info_hash:
![image](https://github.com/user-attachments/assets/4709f881-1618-4367-acde-647909688465)
You will get the SHA1 code and Bittorent Magnet Link:
![image](https://github.com/user-attachments/assets/f6ef88c7-10ab-4b13-acb6-656a3a8edce6)
Mở Bittorent Client Classic (Link download: <a href="[https://stackoverflow.com/questions/5637268/how-do-you-decode-info-hash-information-from-tracker-announce-request](https://www.bittorrent.com/products/win/bittorrent-classic-compare/)" target="_blank">Link</a>), select File and select Add Torrent From URL:
![image](https://github.com/user-attachments/assets/e6c0e028-a83b-49c9-8298-ac3e9b69573d)
Enter the link obtained in the above step to get what you want:
![image](https://github.com/user-attachments/assets/0d87c42e-7e2a-4d69-ba87-1705cc948ed3)
![image](https://github.com/user-attachments/assets/e318fafe-5d7b-46fb-8ea3-72eb38b5947d)
