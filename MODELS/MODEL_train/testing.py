# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 01:33:56 2023

@author: xavid
"""

import torch

def test(model, device, test_loader, MSELoss):

    loss = 0
    # Iterate through test dataset
    with torch.no_grad():
        model.eval()
        for batch_idx, (x,y) in enumerate(test_loader):
            data = x.to(device)
            target = y.to(device)
            output = model(data)
            loss += MSELoss(output, target)

        
        return loss.item()/batch_idx