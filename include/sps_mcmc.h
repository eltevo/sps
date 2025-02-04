#ifndef SPS_MCMC_H
#define SPS_MCMC_H

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <random>
#include <map>
#include <float.h>

#include "sps_write.h" 

class sps_mcmc{
public:

	sps_mcmc();

public:
//functions

	//config file read	
	int read_config(std::string input_filename);

	int control_step_size(double opt_acc);

	int change_params();

	int evaluate_chi(double input_chi);

	int record_data();

	int write_results();


//data
	int iter;

	//chi values
	double chi,chi_before, best_chi;

// diagnostics, results 
	//all the chi values
	std::vector<double> out_chi_evol;
	//best chi values
	std::vector<double> out_best_chi_evol;
	//accepted chi values
	std::vector<double> out_acc_chi_evol;
	//worse than before, but accepted chi values
	std::vector<double> out_worse_acc_chi_evol;
	


	std::vector<double> acc;		//stores the last some accept or nots (0,1)
	std::vector<double> acc_ratio;	// stores averaged acceptance rates
	
	std::vector<double> worse;		//stores the last some worse ot nots (0,1)
	std::vector<double> worse_rate;	// stores averaged rates

	std::vector<double> worse_acc;		//stores the last some worse accept or nots (0,1)
	std::vector<double> worse_acc_ratio;	// stores averaged worse acceptance rates


	//random generator
	std::default_random_engine generator;

	//indicating acceptance
	int accepted;

	//burnin indicator
	bool burnin_ended;

	//maps for parameters
	std::map<std::string,double> parameters;
	std::map<std::string,double> best_parameters;

	//maps for controlling step sizes	
	std::map<std::string,double> steps;
	std::map<std::string,double> sigmas;
	std::map<std::string,std::vector<double> > sigmas_evol;
	std::map<std::string,std::vector<double> > acc_s;
	std::map<std::string,std::vector<double> > acc_ratio_s;
	//an iterator which tells the changer subroutine
	//wich parameter to change
	std::map<std::string,double>::iterator param_iter;
	//an iterator to help it
	int change_iter;

	std::map<std::string,bool> fix_parameters;

	std::map<std::string,double> param_upper_bound;
	std::map<std::string,double> param_lower_bound;

	//map for parameter evolution
	std::map<std::string,std::vector<double> > parameter_evol;
};

#endif
	
