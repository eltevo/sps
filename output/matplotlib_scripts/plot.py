#!/usr/bin/python


import numpy
import matplotlib.pyplot as plt

#reading files
params=dict()
params["dust_tau_v"]=numpy.loadtxt("dust_tau_v.dat")
params["dust_mu"]=numpy.loadtxt("dust_mu.dat")
params["sfr_tau"]=numpy.loadtxt("sfr_tau.dat")
params["age"]=numpy.loadtxt("age.dat")
params["metall"]=numpy.loadtxt("metall.dat")
params["vdisp"]=numpy.loadtxt("vdisp.dat")

fit=numpy.loadtxt("fit.dat")

fig=plt.figure()
#fig.set_size_inches([7,4])
ax=fig.add_subplot(1,1,1)

########################################
#plot fitted and measured spectra
########################################
ax.plot(fit[:,0],fit[:,1],label="measured spectrum")
ax.plot(fit[:,0],fit[:,1]-fit[:,4],label="difference")
ax.plot(fit[:,0],fit[:,4],label="model spectrum")
ax.step(fit[:,0],-10*numpy.sign(fit[:,3]),label="mask")

ax.set_xlim(numpy.amin(fit[:,0]),numpy.amax(fit[:,0]))
ax.set_xlabel("wavelength")
ax.set_ylabel("intensity")
ax.legend(loc="best")

fig.set_size_inches([16,9])
fig.savefig("plots-python/fit.png",dpi=300)

ax.cla()
fig.set_size_inches([8,6])


########################################
#plot parameter evolutions
########################################
for param in params:
	ax.plot(params[param])
	ax.set_xlabel("N")
	ax.set_ylabel(param)
	fig.savefig("plots-python/evol_"+param+".png",dpi=100)
	ax.cla()

########################################
#plot parameter scatters 
########################################
done=dict()
for param1 in params:
	for param2 in params:
		# no diagonal lines
		if(param1 == param2):
			continue
		# no duplicates
		if(done.has_key(param2+param1)):
			continue

		ax.plot(params[param1],params[param2],",")
		ax.set_xlabel(param1)
		ax.set_ylabel(param2)
		fig.savefig("plots-python/scatter_"+param1+"-"+param2+".png",dpi=100)
		ax.cla()
		done[param1+param2]="done"


########################################
#plot parameter histograms 
########################################
N=numpy.float32(len(params["vdisp"]))
nbins=numpy.float32(60)

for param in params:
	binsize=(numpy.amax(params[param])-numpy.amin(params[param]))/nbins

	#create histogram
	hist=numpy.histogram(params[param],nbins)
	#numpy gives bin edges, i delete the last one
	x=numpy.delete(hist[1],-1)

	ax.bar(x,hist[0]/N,binsize*0.8)
	ax.set_ylabel("P")
	ax.set_xlabel(param)
	fig.savefig("plots-python/hist_"+param+".png",dpi=100)
	ax.cla()


