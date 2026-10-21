from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("data/lab4/input.txt") 
print(txt)
write_csv([("word","count"),("test",3)], "data/check.csv") 