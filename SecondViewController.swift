//
//  SecondViewController.swift
//  SpeakToMe
//
//  Created by Sayo Eweje on 10/23/17.
//  Copyright © 2017 Henry Mason. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {

    @IBOutlet weak var FindPatient: UIButton!
    @IBAction func EnterRecord(_ sender: UIButton) {
        performSegue(withIdentifier: "GoToPatientRecord", sender: self)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
