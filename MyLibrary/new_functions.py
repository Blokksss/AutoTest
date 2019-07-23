import httplib

class NewKeywords(object):
	import httplib

	def soap_request(self, host, api, request_data, request_method):


		SoapMessage = """
		< soapenv:Envelope
		xmlns:soapenv = "http://schemas.xmlsoap.org/soap/envelope/"
		xmlns:soap = "http://soap.szkingdom.com/"
		xmlns:xsd = "http://www.w3.org/2001/XMLSchema"
		xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" >
		< soapenv:Header / >
		< soapenv:Body >
		< soap:doService >
		< !--Optional:-->
		< requestXml >
		{}
		< / requestXml >
		< / soap:doService >
		< / soapenv:Body >
		< / soapenv:Envelope >
		"""
		message_to_send = SoapMessage.format(request_data)
		webservice = httplib.HTTP(host)
		webservice.putheader(request_method, api)
		webservice.putheader("Host", host)
		webservice.putheader("User-Agent",
		                     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)")
		webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
		webservice.putheader("Content-length", "%d" % len(SoapMessage))
		webservice.putheader("SOAPAction", "\"http://entinfo.cn/mdsmssend\"")
		webservice.endheaders()  # set headers
		webservice.send(message_to_send)  # send message
		status_code, status_message, header = webservice.getreply()
		return {"status_code": statu_scode, "status_message": status_message, "header": header}