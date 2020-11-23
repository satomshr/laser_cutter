#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import svgwrite


# In[2]:


# http://kijishi.html.xdomain.jp/komanosize.htm
# https://rskmoi.hatenablog.com/entry/2018/01/21/104029
c = 28.2
mu_c = 31.0
mu = mu_c / c

Q_deg = 115.0
R_deg = 80.4
P_deg = (540 - (Q_deg * 2 + R_deg))/2

P, Q, R = np.deg2rad([P_deg, Q_deg, R_deg])
a = c * (mu * np.cos(R) - np.sin(R)/2) / np.cos(P/2 + R)


# In[3]:


P_deg


# In[4]:


# https://blog.goo.ne.jp/m4g/e/8a18befcb3b83efaca95803cded4b28b
q_x = a * np.sin(P/2)
q_y = a * np.cos(P/2)
r_x = c/2
r_y = mu_c


# In[5]:


points = []
points.append([0, 0])
points.append([q_x, q_y])
points.append([r_x, r_y])
points.append([-r_x, r_y])
points.append([-q_x, q_y])


# In[6]:


dwg = svgwrite.Drawing("shogi.svg")
dwg.add( dwg.polygon( points=points ) )
dwg.save()

