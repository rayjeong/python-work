import dns.resolver
#answer=dns.resolver.query("google.com", "A")
#for data in answer:
#    print data.address


answers = dns.resolver.query('ansible', 'CNAME')
print ' query qname:', answers.qname, ' num ans.', len(answers)
for rdata in answers:
    print ' cname target address:', rdata.target
