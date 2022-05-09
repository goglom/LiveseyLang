# LiveseyLang
Implemenation of very simple translator of Dr. Dr. Livesey languge (from russian and to russian).
This language based on Huffman coding with alphabet - {'А', 'Х'}


![AXAXAXAX](https://i.pinimg.com/736x/cb/51/ce/cb51ce1791321f318a8d9192191c03c2.jpg)

# How to use

```python
>> res = russian_to_livesey("Привет", "мир")
>> print(res)
>> print(livesey_to_russian(*res))

['ХХАААххахаххааахаххххаххх', 'хааахаххаххах']
['Привет', 'мир']
```
