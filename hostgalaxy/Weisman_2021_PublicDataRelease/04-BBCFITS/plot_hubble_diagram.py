import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("SALT2mu_DES+LOWZ_G10.FITRES", sep='\s+', skiprows=7, comment="#")
mu = data["mB"] + 0.1 * data["x1"] - 3.1 * data["c"] + 19.3

m = pd.read_csv("SALT2mu_DES+LOWZ_G10.M0DIF", sep='\s+', skiprows=11, comment="#")
bin_z, bin_mu, bin_err = m["z"], m["MUREF"] + m["MUDIF"], m["MUDIFERR"]
mask = bin_err < 1

fig, ax = plt.subplots()
ax.scatter(data["zHD"], mu, s=3, c=data["c"], label="SN", alpha=0.2)
ax.errorbar(bin_z[mask], bin_mu[mask], yerr=bin_err[mask], fmt="o", c='k', ms=2, label="Binned")
ax.set_xlabel("z")
ax.set_ylabel("mu")
ax.legend(loc=4, frameon=False)
