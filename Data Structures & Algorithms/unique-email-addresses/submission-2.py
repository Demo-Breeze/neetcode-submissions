class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = set()
        for email in emails:
            local,domain = email.split("@")
            local = local.replace(".","")
            if "+" in local:
                l = local.index("+")
                local = local[0:l]
            answer.add(f"{local}@{domain}")
        return len(answer)