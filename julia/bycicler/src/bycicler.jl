module bycicler

using JSON
using HTTP
using DataFrames

res = HTTP.get("http://api.citybik.es/v2/networks/bicing?fields=stations")

status, headers, body = res.status, res.headers , String(res.body)

res_str = JSON.Parser.parse(String(res.body))

res_json = JSON.Parser.parse(res_str)

jtable = JSONTables.jsontable(String(res.body))

greet() = print("Hello World!")

end # module
