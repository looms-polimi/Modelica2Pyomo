true
""
true
""
true
""
"//! base 0.1.0
package 'TestFullModel2VolsNoNormNoRamp'
  model 'TestFullModel2VolsNoNormNoRamp'
    Real 'wCold.y' \"Value of Real output\";
    Real 'wHot.y' \"Value of Real output\";
    Real 'Pel.y' \"Value of Real output\";
    Real 'TIT.y' \"Value of Real output\";
    parameter Integer 'completeModel.n' = 2;
    parameter Real 'completeModel.pOutTurb'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\") = 8e6;
    parameter Real 'completeModel.pOutHotHX'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\") = 1.2e5;
    parameter Real 'completeModel.TinCold'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\") = 723.15;
    parameter Real 'completeModel.TinHot'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\") = 1413.15;
    parameter Real 'completeModel.ToutColdStart'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\") = 891.15;
    parameter Real 'completeModel.ToutHotStart'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\") = 733.15;
    parameter Real 'completeModel.kCold'(unit = \"Pa/(kg/s)\") = 900.0;
    parameter Real 'completeModel.kHot'(unit = \"Pa/(kg/s)\") = 50.0;
    parameter Real 'completeModel.pNomCold'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\") = 2.5e7;
    parameter Real 'completeModel.pNomHot'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\") = 1.2e5;
    parameter Real 'completeModel.wNomCold'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\") = 270.0;
    parameter Real 'completeModel.wNomHot'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\") = 62.0;
    parameter Real 'completeModel.gammaNomCold'(nominal = 5000.0, min = 0.0, unit = \"W/(m2.K)\", quantity = \"CoefficientOfHeatTransfer\") = 3400.0;
    parameter Real 'completeModel.gammaNomHot'(nominal = 5000.0, min = 0.0, unit = \"W/(m2.K)\", quantity = \"CoefficientOfHeatTransfer\") = 90.0;
    parameter Real 'completeModel.alpha' = 0.5;
    parameter Real 'completeModel.beta' = 0.8;
    parameter Real 'completeModel.cW'(nominal = 500.0, unit = \"J/(kg.K)\", quantity = \"SpecificHeatCapacity\") = 590.0;
    parameter Real 'completeModel.Mw'(nominal = 100.0, min = 0.0, unit = \"kg\", quantity = \"Mass\") = 231000.0;
    parameter Real 'completeModel.Scold'(nominal = 10.0, unit = \"m2\", quantity = \"Area\") = 3046.5;
    parameter Real 'completeModel.Shot'(nominal = 10.0, unit = \"m2\", quantity = \"Area\") = 3046.5;
    parameter Real 'completeModel.Vcold'(nominal = 10.0, unit = \"m3\", quantity = \"Volume\") = 52.0;
    parameter Real 'completeModel.Vhot'(nominal = 10.0, unit = \"m3\", quantity = \"Volume\") = 13292.0;
    parameter Real 'completeModel.Kt'(nominal = 10.0, unit = \"m2\", quantity = \"Area\") = 0.0045;
    parameter Real 'completeModel.eta_iso_nom'(min = 0.0, unit = \"1\", quantity = \"Efficiency\") = 0.843;
    parameter Real 'completeModel.ToutTurbStart'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\") = 763.15;
    parameter Real 'completeModel.eta_mech'(min = 0.0, unit = \"1\", quantity = \"Efficiency\") = 0.98 \"Mechanical efficiency\";
    parameter Real 'completeModel.eta_elec'(min = 0.0, unit = \"1\", quantity = \"Efficiency\") = 0.996 \"Nominal Electrical efficiency\";
    constant Real 'completeModel.MMco2'(nominal = 0.0440095, min = 0.0, unit = \"kg/mol\", quantity = \"MolarMass\") = 0.0440095;
    constant Real 'completeModel.MMflue'(nominal = 0.0440095, min = 0.0, unit = \"kg/mol\", quantity = \"MolarMass\") = 0.029076969929450615;
    constant Real 'completeModel.Rcold'(unit = \"J/(kg.K)\") = 188.92426903630442;
    constant Real 'completeModel.Rhot'(unit = \"J/(kg.K)\") = 285.9466663248131;
    constant Real 'completeModel.cpCold'(nominal = 1000.0, unit = \"J/(kg.K)\", quantity = \"SpecificHeatCapacity\") = 1170.0;
    constant Real 'completeModel.cpHot'(nominal = 1000.0, unit = \"J/(kg.K)\", quantity = \"SpecificHeatCapacity\") = 1260.0;
    constant Real 'completeModel.cvCold'(nominal = 1000.0, unit = \"J/(kg.K)\", quantity = \"SpecificHeatCapacity\") = 981.0757309636956;
    constant Real 'completeModel.cvHot'(nominal = 1000.0, unit = \"J/(kg.K)\", quantity = \"SpecificHeatCapacity\") = 974.0533336751869;
    Real 'completeModel.pCold'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.pHot'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.pInCold'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.pInHot'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.pOutCold'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.pOutHot'(nominal = 1e7, displayUnit = \"bar\", unit = \"Pa\", quantity = \"Pressure\");
    Real 'completeModel.wCold[1]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.wCold[2]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.wCold[3]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.wHot[1]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.wHot[2]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.wHot[3]'(nominal = 100.0, unit = \"kg/s\", quantity = \"MassFlowRate\");
    Real 'completeModel.Tcold[1]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Tcold[2]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Tcold[3]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Thot[1]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Thot[2]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Thot[3]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Twall[1]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.Twall[2]'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
    Real 'completeModel.wInCold';
    Real 'completeModel.wInHot';
    Real 'completeModel.Pel'(nominal = 1e7, unit = \"W\", quantity = \"Power\");
    Real 'completeModel.TIT'(nominal = 500.0, start = 288.15, min = 0.0, displayUnit = \"degC\", unit = \"K\", quantity = \"ThermodynamicTemperature\");
  initial equation
    der('completeModel.Twall[1]') = 0.0;
    der('completeModel.Twall[2]') = 0.0;
    der('completeModel.Tcold[1]') = 0.0;
    der('completeModel.Tcold[2]') = 0.0;
    der('completeModel.Tcold[3]') = 0.0;
    der('completeModel.Thot[1]') = 0.0;
    der('completeModel.Thot[2]') = 0.0;
    der('completeModel.Thot[3]') = 0.0;
    der('completeModel.pCold') = 0.0;
    der('completeModel.pHot') = 0.0;
  equation
    'wCold.y' = 270.0;
    'wHot.y' = 62.0;
    'Pel.y' = 'completeModel.Pel';
    'TIT.y' = 'completeModel.TIT';
    'wCold.y' = 'completeModel.wInCold';
    'wHot.y' = 'completeModel.wInHot';
    'completeModel.wInCold' = 'completeModel.wCold[1]';
    'completeModel.wInHot' = 'completeModel.wHot[1]';
    'completeModel.Tcold[1]' = 723.15;
    'completeModel.Thot[1]' = 1413.15;
    'completeModel.pOutHot' = 1.2e5;
    'completeModel.pInCold' - 'completeModel.pCold' = 450.0 * 'completeModel.wCold[1]';
    'completeModel.pCold' - 'completeModel.pOutCold' = 450.0 * 'completeModel.wCold[3]';
    'completeModel.pInHot' - 'completeModel.pHot' = 25.0 * 'completeModel.wHot[1]';
    'completeModel.pHot' - 'completeModel.pOutHot' = 25.0 * 'completeModel.wHot[3]';
    26.0 / (188.92426903630442 * 'completeModel.Tcold[2]') * der('completeModel.pCold') = 'completeModel.wCold[1]' - 'completeModel.wCold[2]';
    6646.0 / (285.9466663248131 * 'completeModel.Thot[2]') * der('completeModel.pHot') = 'completeModel.wHot[1]' - 'completeModel.wHot[2]';
    'completeModel.pCold' / 188.92426903630442 / 'completeModel.Tcold[2]' * 52.0 / 2.0 * 981.0757309636956 * der('completeModel.Tcold[2]') = 'completeModel.wCold[2]' * 1170.0 * ('completeModel.Tcold[1]' - 'completeModel.Tcold[2]') + 3400.0 * ('completeModel.pOutCold' / 2.5e7) ^ 0.5 * ('completeModel.wCold[2]' / 270.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[1]' - ('completeModel.Tcold[1]' + 'completeModel.Tcold[2]') / 2.0);
    'completeModel.pHot' / 285.9466663248131 / 'completeModel.Thot[2]' * 13292.0 / 2.0 * 974.0533336751869 * der('completeModel.Thot[2]') = 'completeModel.wHot[2]' * 1260.0 * ('completeModel.Thot[1]' - 'completeModel.Thot[2]') + 90.0 * ('completeModel.pOutHot' / 1.2e5) ^ 0.5 * ('completeModel.wHot[2]' / 62.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[2]' - ('completeModel.Thot[1]' + 'completeModel.Thot[2]') / 2.0);
    6.8145e7 * der('completeModel.Twall[1]') = -(3400.0 * ('completeModel.pOutCold' / 2.5e7) ^ 0.5 * ('completeModel.wCold[2]' / 270.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[1]' - ('completeModel.Tcold[1]' + 'completeModel.Tcold[2]') / 2.0) + 90.0 * ('completeModel.pOutHot' / 1.2e5) ^ 0.5 * ('completeModel.wHot[2]' / 62.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[1]' - ('completeModel.Thot[3]' + 'completeModel.Thot[2]') / 2.0));
    26.0 / (188.92426903630442 * 'completeModel.Tcold[3]') * der('completeModel.pCold') = 'completeModel.wCold[2]' - 'completeModel.wCold[3]';
    6646.0 / (285.9466663248131 * 'completeModel.Thot[3]') * der('completeModel.pHot') = 'completeModel.wHot[2]' - 'completeModel.wHot[3]';
    'completeModel.pCold' / 188.92426903630442 / 'completeModel.Tcold[3]' * 52.0 / 2.0 * 981.0757309636956 * der('completeModel.Tcold[3]') = 'completeModel.wCold[3]' * 1170.0 * ('completeModel.Tcold[2]' - 'completeModel.Tcold[3]') + 3400.0 * ('completeModel.pOutCold' / 2.5e7) ^ 0.5 * ('completeModel.wCold[3]' / 270.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[2]' - ('completeModel.Tcold[2]' + 'completeModel.Tcold[3]') / 2.0);
    'completeModel.pHot' / 285.9466663248131 / 'completeModel.Thot[3]' * 13292.0 / 2.0 * 974.0533336751869 * der('completeModel.Thot[3]') = 'completeModel.wHot[3]' * 1260.0 * ('completeModel.Thot[2]' - 'completeModel.Thot[3]') + 90.0 * ('completeModel.pOutHot' / 1.2e5) ^ 0.5 * ('completeModel.wHot[3]' / 62.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[1]' - ('completeModel.Thot[2]' + 'completeModel.Thot[3]') / 2.0);
    6.8145e7 * der('completeModel.Twall[2]') = -(3400.0 * ('completeModel.pOutCold' / 2.5e7) ^ 0.5 * ('completeModel.wCold[3]' / 270.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[2]' - ('completeModel.Tcold[2]' + 'completeModel.Tcold[3]') / 2.0) + 90.0 * ('completeModel.pOutHot' / 1.2e5) ^ 0.5 * ('completeModel.wHot[1]' / 62.0) ^ 0.8 * 3046.5 / 2.0 * ('completeModel.Twall[2]' - ('completeModel.Thot[2]' + 'completeModel.Thot[1]') / 2.0));
    'completeModel.wCold[3]' = 0.0045 * 'completeModel.pOutCold' * sqrt(0.0052931262092528525 / 'completeModel.Tcold[3]') * sqrt(1.0 - (1.0 / ('completeModel.pOutCold' / 8e6)) ^ 2.0);
    'completeModel.Pel' = 'completeModel.wCold[3]' * 0.843 * 1170.0 * 'completeModel.Tcold[3]' * (1.0 - (8e6 / 'completeModel.pOutCold') ^ 0.1614737342190636) * 0.98 * 0.996;
    'completeModel.TIT' = 'completeModel.Tcold[3]';
    annotation(experiment(StopTime = 4000, __Dymola_NumberOfIntervals = 5000, __Dymola_Algorithm = \"Dassl\"));
  end 'TestFullModel2VolsNoNormNoRamp';
end 'TestFullModel2VolsNoNormNoRamp';
"
""
