from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashMap = {}
        for email in emails:
            local,domain = email.split('@')
            local = local.replace('.','')

            plus_index = local.find('+')
            if plus_index != -1:
                local = local[:plus_index]            
                
            reconstructed_email = local + '@' + domain
            if(reconstructed_email in hashMap):
                pass
            else:
                hashMap[reconstructed_email] = reconstructed_email

        return len(hashMap)