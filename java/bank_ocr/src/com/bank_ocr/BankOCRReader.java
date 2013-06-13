package com.bank_ocr;

import java.util.*;

/**
 * Created with IntelliJ IDEA.
 * User: nielsm
 * Date: 5/29/13
 * Time: 1:04 PM
 * To change this template use File | Settings | File Templates.
 */
public class BankOCRReader {

    private static final Map<String, String> digitRepresentations;
    private static int numberWidth = 3;
    private static int numberHeight = 3;
    static {
        HashMap<String, String> aMap = new HashMap<String, String>();
        aMap.put("  |" +
                "  |" +
                "  |", "1");
        aMap.put(" _ " +
                " _|" +
                "|_ ", "2");
        aMap.put(" _ " +
                " _|" +
                " _|", "3");

        digitRepresentations = Collections.unmodifiableMap(aMap);
    }

    String getDigit(String chunk) {
        if (digitRepresentations.containsKey(chunk)) {
            return digitRepresentations.get(chunk);
        } else {
            return "?";
        }
    }

    String getChunk(String[] splitNumber, int start) {
        StringBuffer stringBuffer = new StringBuffer();

        for (int x = 0; x < numberHeight; ++x) {
            stringBuffer.append(splitNumber[x].substring(start, start + numberWidth));
        }

        return stringBuffer.toString();

    }

    List<String> chunkNumberString(String wholeNumber) {
        String[] splitString = wholeNumber.split(System.getProperty("line.separator"));

        int chunkNumber = splitString[0].length() / numberWidth;

        List<String> result = new ArrayList<String>();

        for (int x = 0; x < chunkNumber; ++x) {
            result.add(getChunk(splitString, x * numberWidth));
        }

        return result;
    }

    String convertToNumber(String inputNumber) {
        List<String> digitChunks = chunkNumberString(inputNumber);
        StringBuffer result = new StringBuffer();

        for (String chunk : digitChunks) {
            result.append(getDigit(chunk));
        }

        return result.toString();
    }

    String[] splitNumber(String inputNumbers) {
        String eol = System.getProperty("line.separator");
        return inputNumbers.split(eol + eol);
    }

    List<String> convertToNumbers(String inputNumbers) {
        String [] numberStringList = splitNumber(inputNumbers);
        List<String> result = new ArrayList<String>();

        for (String numberString : numberStringList) {
            result.add(convertToNumber(numberString));
        }

        return result;
    }
}
