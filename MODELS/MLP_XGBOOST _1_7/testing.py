# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:03:29 2023

@author: xavid
"""

import torch

def test(model, device, test_loader, MSELoss):

    loss = 0
    # Iterate through test dataset
    with torch.no_grad():
        model.eval()
        for batch_idx, (X_meteo_eto, pred_xgboost, y) in enumerate(test_loader):
            
            data1 = X_meteo_eto.to(device)
            data2 = pred_xgboost.to(device)
            target = y.to(device)

            output, _ = model(data1, data2)
            loss += MSELoss(output.view([-1]), target)

        
        return loss.item()
    
    
import torch

def test2(model_prev, model, device, test_loader, MSELoss):

    loss = 0
    # Iterate through test dataset
    with torch.no_grad():
        model.eval()
        for batch_idx, (X_meteo_eto, pred_xgboost, y, superficie) in enumerate(test_loader):
            
            data1 = X_meteo_eto.to(device)
            data2 = pred_xgboost.to(device)
            data3 = superficie.to(device)
            target = y.to(device)
            
            _, output_first_mlp = model_prev(data1, data2)
            
            output = model(data1, data2, output_first_mlp, data3)
            loss += MSELoss(output.view([-1]), target)

        
        return loss.item()