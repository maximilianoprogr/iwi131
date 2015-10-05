import urllib2

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

download_file("http://progra.usm.cl/Archivos/certamenes/Libro_prograRB.pdf")


