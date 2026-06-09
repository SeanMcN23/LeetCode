class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        # valid email consists of a local name and domain name serperated by the '@' sign, email may contain . or +

        # so the +, everything after the plus but before the @ can be safely ignored basically, periods in the name can be ignored but not the domain

        # so in my brain im thinking we need to take care of 2 seperate fallacies here. everything before the @ and after

        #  dictionary, we will store the domain as key, but names as values

        
        email2=set()
        for email in emails:
            name,domain= email.split("@")
            name=name.split("+")[0]
            name=name.replace('.',"")

            email2.add((name,domain))
        return len(email2)
           
        
        
        
        
     





