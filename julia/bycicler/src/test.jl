include("bycicler.jl")
import .bycicler

res = bycicler.convert_data("http://api.citybik.es/v2/networks/bicing?fields=stations")
res


