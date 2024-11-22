# Flow: https://stackoverflow.com/questions/5637268/how-do-you-decode-info-hash-information-from-tracker-announce-request
# Author: KhanhCQ
# Date: 21/11/2024
# Country: VietNam
def decode_info_hash(info_hash):
    decoded = ""
    i = 0
    while i < len(info_hash):
        if info_hash[i] == "%":  # If the % character is encountered, take the next 2 characters.
            hex_value = info_hash[i + 1:i + 3]
            decoded += hex_value
            i += 3  # Jump 3 characters
        else:  # If not %, convert lowercase character to hex code
            decoded += format(ord(info_hash[i]), "02x")
            i += 1  # Jump over lowercase characters
    return decoded

def generate_magnet_link(info_hash, name):
    base_url = "magnet:"
    xt = f"xt=urn:btih:{info_hash}"
    dn = f"dn={name}"
    trackers = [
        "udp://tracker.openbittorrent.com:80",
        "udp://opentor.org:2710",
        "udp://tracker.ccc.de:80",
        "udp://tracker.blackunicorn.xyz:6969",
        "udp://tracker.coppersurfer.tk:6969",
        "udp://tracker.leechers-paradise.org:6969",
    ]
    tr = "&".join([f"tr={tracker.replace(':', '%3A').replace('/', '%2F')}" for tracker in trackers])
    return f"{base_url}?{xt}&{dn}&{tr}"

info_hash_payload = input("Input info_hash: ")
file_name = ""
decoded_info_hash = decode_info_hash(info_hash_payload)
magnet_link = generate_magnet_link(decoded_info_hash, file_name)
print("Decoded info_hash:", decoded_info_hash)
print("Magnet link:", magnet_link)
