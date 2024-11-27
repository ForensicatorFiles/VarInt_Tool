# VarInt_Tool
This simple command line tool can take a Hexadecimal or Integer as input and output the unsigned and signed VarInt.

Useage:

  Hexadecimal Value
  
  `python varint_tool.py 0xE4B2F8B801`

  Output:
  
    Hexadecimal Input: 0xE4B2F8B801
    Decoded Unsigned Varint: 387848548
    Decoded Signed Varint (32-bit): 387848548
    
  Hexadecimal Value:
  
  `python varint_tool.py 0xCAC6CE8FFDFFFFFFFF01`

  Output:
  
    Hexadecimal Input: 0xCAC6CE8FFDFFFFFFFF01
    Decoded Unsigned Varint: 18446744072936989514
    Decoded Signed Varint (32-bit): -772562102


  Unsigned Integer Value
  
  `python varint_tool.py 387848548`
  
  Output:
  
    Unsigned Varint Input: 387848548
    Encoded Hexadecimal: 0xE4B2F8B801
    Decoded Signed Varint (32-bit): 387848548

  
