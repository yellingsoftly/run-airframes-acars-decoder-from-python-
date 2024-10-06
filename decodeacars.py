from javascript import require
import json 
import sys

my_module = require("@airframes/acars-decoder")






decobj = my_module.MessageDecoder() 


def make_input_data(id_name, encoded_text):
    #return data structure for sending to decoder
    
    return {'label': id_name, 'text': encoded_text}
    
    
def convert_decoded_results(result):
    #convert decoded results to output file
    
    results = dict.fromkeys(['preface', 'message_1'])
    
    results['preface'] = result.raw
    results['message_1'] = result.formatted
    
    return results


def run_all_decode(id_name, encoded_text):

    data = make_input_data(id_name, encoded_text)
    
    decoded = decobj.decode(data)
    
    result_parsed = convert_decoded_results(decoded)
    
    print(result_parsed)

    with open(f'id_name', 'w') as file:
        json.dumps(result_parsed)



module = my_module.MessageDecoder

print(module)

if __name__ == '__main__':
    from javascript import require
    import json 

    my_module = require("@airframes/acars-decoder")
    
    decobj = my_module.MessageDecoder()
    
    
    message_Label = 'H1' # Message label
    encoded = "POSN39255W081432,VLA01,152602,360,EMP01,153707,MEC01,M50,275053,162464D" #Non decoded message
    run_all_decode(message_Label, encoded)
    