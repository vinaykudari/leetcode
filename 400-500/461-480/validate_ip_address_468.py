# Math

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_valid_IPV4(IP):
            IP_split = IP.split('.')
            if len(IP_split) != 4:
                return "Neither"
            for num in IP_split:
                if not num.isdigit() or num != str(int(num)) or int(num) > 255 or int(num) < 0:
                    return "Neither"
            return 'IPv4'
        
        def is_hex(num):
            try:
                int(num, 16)
                return num[0] != '-'
            except ValueError:
                return False
                
        def is_valid_IPV6(IP):
            IP_split = IP.split(':')
            if len(IP_split) != 8:
                return "Neither"
            for num in IP_split:
                if not is_hex(num) or len(num) == 0 or len(num) > 4:
                    return "Neither"
            return "IPv6"
        
        if len(IP) < 4:
            return "Neither"
        
        if IP[3] == '.':
            return is_valid_IPV4(IP)
        
        return is_valid_IPV6(IP)
