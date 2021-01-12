module bycicler

using JSON
using HTTP
using DataFrames

function get_data(url)
    res = HTTP.get(url)
    res_str = String(res.body)
    res_array = JSON.Parser.parse(res_str)["network"]["stations"]
    res_array
end

function dict2df(dict)
    extra = dict["extra"]
    delete!(dict, "extra")
    hcat(
        DataFrames.DataFrame(dict),
        DataFrames.DataFrame(extra)
    )
end

function convert_data(url)
    res_array = get_data(url)
    res = vcat(map(dict2df, res_array)...)
    res
end

end # module
