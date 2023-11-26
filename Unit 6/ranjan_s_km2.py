import sys; args = sys.argv[1:]
from PIL import Image; img = Image.open(args[0])
import PIL
# import urllib.request
import random
# import tkinter as tk io, sys, os,
# from PIL import Image, ImageTk # Place this at the end (to avoid any conflicts/errors)

def choose_random_means(k, img, pix):
   means = [pix[(int)(random.uniform(0, img.size[0]-1)),(int)(random.uniform(0, img.size[1]-1))] for i in range(k)]
   return means

# goal test: no hopping
def check_move_count(mc):
    for z in mc:
        if z == 0:
            return True
    return False

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means):
   minIndex, dist_sum = 0, 255**2+255**2+255**2
   for d in range(len(means)):
      dist = ((means[d][0]-col[0])**2 + (means[d][1]-col[1])**2 + (means[d][2]-col[2])**2) ** 0.5 #dist formula
      if dist_sum > dist:
         minIndex = d
         dist_sum = dist
   return minIndex 

def clustering(img, pix, temp, cb, mc, means, count):
   temp_pb, temp_mc, temp_m = [[] for x in means], [], []
   temp_cb = [0 for x in means]
   for color in temp: 
      temp_dist = dist(color, means)
      temp_pb[temp_dist].append(color)  
      temp_cb[temp_dist] += 1 
   temp_mc = [ (a-b) for a, b in zip(temp_cb, cb)]

   for part in temp_pb: #gets individual color sums
      sum_r, sum_g, sum_b = 0, 0, 0
      for sub in part:
         sum_r += sub[0]
         sum_g += sub[1]
         sum_b += sub[2]
      temp_m.append((sum_r / len(part), sum_g / len(part), sum_b / len(part)))
  # print ('diff', count, ':', temp_mc)
   return temp_cb, temp_mc, temp_m

def update_picture(img, pix, means):
   region_dict = {}
   for p in range(img.size[0]):
       for x in range(img.size[1]):
           color = pix[p,x]
           index = dist(color, means)
           pix[p,x] = (int)(means[index][0]),(int)(means[index][1]),(int)(means[index][2])
   #     for everypix in img:
   #         everypix = means[p]
   #         region_dict.append(everypix)
   return pix, region_dict
   
def distinct_pix_count(img, pix):
    cols = {}
    max_col, max_count = pix[0, 0], 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pix[i, j] not in cols.keys():
                cols[pix[i, j]] = 1
            else:
                cols[pix[i, j]] += 1
    for col in cols.keys():
        if cols[col] > max_count:
            max_col = col
            max_count = cols[col]
    return len(cols.keys()), max_col, max_count, cols.keys()

def count_regions(img, region_dict, pix, means):
   region_count = [0 for x in means]
   
   return region_count

 
def main():
   #k = 4 int(sys.argv[1])
   k= int(args[1])
   #file = sys.argv[2]
   # file = args[1]
   #if not os.path.isfile(file):
   #   file = io.BytesIO(urllib.request.urlopen(file).read())
   
   # window = tk.Tk() #create an window object
   # img2 = Image.open(file)
   # img = Image.open(file)7
   # img_tk = ImageTk.PhotoImage(img)
   # img_tk2 = ImageTk.PhotoImage(img2)
   # lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   # lbl2 = tk.Label(window, image = img_tk2).pack()  # display the image at window
   temp = [] #i need a place to keep the colors values
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count, temp = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = choose_random_means(k, img, pix)
   print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = clustering(img, pix, temp, count_buckets, move_count, means, count)
      if count == 2:
         print ('first means:', means)
         print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means)  # region_dict can be an empty dictionary
   print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (i+1, ':', means[i], '=>', count_buckets[i])
      
   # img_tk = ImageTk.PhotoImage(img)
   # lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
# ll = tk.Label(window, image = img).pack()

   img.save("kmeans/{}.png".format("2023sranjan"), "PNG")  # change to your own filename
   # window.mainloop()
   #img.show()
   
if __name__ == '__main__': 
   main()
#Simrith Ranjan, Pd 5, 2023