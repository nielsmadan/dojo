package com.bank_ocr;

import java.util.ArrayList;
import java.util.List;

public class BankOCR {
    Boolean isValidAccountNumberChecksum(String accountNumber) {
        int result = 0;

        for (int x = 0; x < accountNumber.length(); ++x) {
            result += (accountNumber.length() - x) * Integer.decode(accountNumber.substring(x, x + 1));
        }

        return result % 11 == 0;
    }

    Boolean isLegibleAccountNumber(String accountNumber) {
        return !accountNumber.contains("?");
    }

    String getNumberResultOutput(String accountNumber) {
        if (!isLegibleAccountNumber(accountNumber)) return accountNumber + " ILL";
        if (!isValidAccountNumberChecksum(accountNumber)) return accountNumber + " ERR";

        return accountNumber;
    }

    List<String> getNumberListValidationOutput(List<String> accountNumberList) {
        List<String> result = new ArrayList<String>();

        for (String accountNumber : accountNumberList) {
            result.add(getNumberResultOutput(accountNumber));
        }

        return result;
    }
}
