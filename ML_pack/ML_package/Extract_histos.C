//Macro to extract the relevant histograms from the produced simulation files

#include "TFile.h"
#include "TF1.h"
#include "TH1.h"
#include "TCanvas.h"
#include <fstream>
#include "TGraph.h"
#include "TGraphErrors.h"

#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void Extract_histos(string root_dump, string hist_dump, const char* filename) {

  //Define variables for filename vector
  std::vector<std::string> filenames;
  std::stringstream ss(filename);
  std::string item;
  
  //Loop over filenames string and add to c++ vector
  while (std::getline(ss, item, ' ')){
    filenames.push_back(item);
    }


  int count = 0;  
  for (size_t i = 0; i < filenames.size(); ++i){

    //Get filename and append to directory name
    string fname = root_dump + "/" + filenames[i];
    std::cout << filenames[i] << endl;
    
    //Define in file
    TFile *fin = new TFile(fname.c_str());

    //Get part of file name with file number to append to outfile name
    std::vector<std::string> tokens;
    std::string file;
    file = filenames[i];
    for (std::stringstream ss(filenames[i]); std::getline(ss, filenames[i], '_'); tokens.push_back(filenames[i]));
  
    //Define output file name
    string fout_name = hist_dump + "/" + "sim_" + tokens[1] + "_2D.root";
    TFile *fout = new TFile(fout_name.c_str(),"RECREATE");

  
    //Get histograms
    TH2D *hClover_gg = (TH2D*)fin->Get("hClover_gg");
    TH2D *hClover_gg_esum = (TH2D*)fin->Get("hClover_gg_esum");

    //Write histograms to out file and increase loop iterator by 1
    fout->cd();
    hClover_gg->Write();
    hClover_gg_esum->Write();
    fout->Write();
    count++;
  }

}
