from transaction2 import  add_beneficiary, fund_transfer, remove_beneficiary, view_beneficiary_list
def test_case2():
    assert(add_beneficiary("Ankitha", "001"))
    assert(add_beneficiary("Ancy", "002"))
    assert(add_beneficiary("Abhi", "003"))
    beneficiaries=view_beneficiary_list()
    print(beneficiaries)
    assert "Ancy" in beneficiaries
    assert(fund_transfer("Ankitha",5000))
    assert(remove_beneficiary("Ancy"))
    updated_list=view_beneficiary_list()
    print(updated_list)
    assert "Ancy" not in updated_list
    