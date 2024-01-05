# Credit Risk Models

### Topics
- Structural v Reduced Form Models
- Hazard Rate / Default Intensity 
- Real World v Risk Neutral Default Probabilities
- Logistic Regression for probability of default
- Recovery Rate and Probability of Default Independence
- Vasichek Model for Credit Risk Capital
- Netting Factor
- xVA : Introduction
- Credit Exposure Metrics
- Credit Exposure Metrics for IRS

**Types**
1. **Structural Model** - why default occurs? default endogenous - option pricing
2. **Reduced Form Model** - when does default occur? default exogenous - statistical models.\
Default intensity - conditional probability of default over a small time period assuming no default upto this point
Better fit to the actual model

### Credit Risk Metrics
1. EFV : Expected Future Value
2. EE: Expected Exposure
2. PFE: Positive Future Exposure - helps setting credit limit - like VAR
3. EPE : Expected positive exposure - average amount the CPTY would owe if we defualt at a  time t - Input to CVA
4. ENE : Expected positive exposure - average amount  I would owe if CPTY defualt at a time t - Input to DVA

5. EEE : Effective Expected Exposure:  "Roll Over Risk " causes underestimation of expected exposures. Since risk is going to be rolled over we need to fill in the troughs