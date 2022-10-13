OPENQASM 2.0;
include "qelib1.inc";
qreg q[36];
u2(0,pi) q[2];
u2(0,pi) q[5];
u2(0,pi) q[8];
u2(0,pi) q[9];
u2(0,pi) q[12];
u2(0,pi) q[15];
u2(0,pi) q[16];
u2(0,pi) q[19];
u2(0,pi) q[20];
u2(0,pi) q[23];
u2(0,pi) q[24];
u2(0,pi) q[27];
u2(0,pi) q[30];
u2(0,pi) q[31];
u2(0,pi) q[34];
u1(pi/4) q[0];
u1(pi/4) q[1];
cx q[2],q[0];
cx q[1],q[2];
u1(-pi/4) q[0];
u1(-pi/4) q[2];
cx q[1],q[0];
cx q[1],q[2];
u1(pi/4) q[0];
cx q[2],q[0];
u1(-pi/4) q[0];
u1(pi/4) q[2];
cx q[1],q[0];
u1(pi/4) q[3];
u1(pi/4) q[4];
cx q[5],q[3];
cx q[4],q[5];
u1(-pi/4) q[3];
u1(-pi/4) q[5];
cx q[4],q[3];
cx q[4],q[5];
u1(pi/4) q[3];
cx q[5],q[3];
u1(-pi/4) q[3];
u1(pi/4) q[5];
cx q[4],q[3];
u1(pi/4) q[6];
u1(pi/4) q[7];
cx q[9],q[6];
cx q[7],q[9];
u1(-pi/4) q[6];
u1(-pi/4) q[9];
cx q[7],q[6];
cx q[7],q[9];
u1(pi/4) q[6];
cx q[9],q[6];
u1(-pi/4) q[6];
u1(pi/4) q[9];
cx q[7],q[6];
u1(pi/4) q[10];
u1(pi/4) q[11];
cx q[12],q[10];
cx q[11],q[12];
u1(-pi/4) q[10];
u1(-pi/4) q[12];
cx q[11],q[10];
cx q[11],q[12];
u1(pi/4) q[10];
cx q[12],q[10];
u1(-pi/4) q[10];
u1(pi/4) q[12];
cx q[11],q[10];
u1(pi/4) q[13];
u1(pi/4) q[14];
cx q[16],q[13];
cx q[14],q[16];
u1(-pi/4) q[13];
u1(-pi/4) q[16];
cx q[14],q[13];
cx q[14],q[16];
u1(pi/4) q[13];
cx q[16],q[13];
u1(-pi/4) q[13];
u1(pi/4) q[16];
cx q[14],q[13];
u1(pi/4) q[17];
u1(pi/4) q[18];
cx q[20],q[17];
cx q[18],q[20];
u1(-pi/4) q[17];
u1(-pi/4) q[20];
cx q[18],q[17];
cx q[18],q[20];
u1(pi/4) q[17];
cx q[20],q[17];
u1(-pi/4) q[17];
u1(pi/4) q[20];
cx q[18],q[17];
u1(pi/4) q[21];
u1(pi/4) q[22];
cx q[24],q[21];
cx q[22],q[24];
u1(-pi/4) q[21];
u1(-pi/4) q[24];
cx q[22],q[21];
cx q[22],q[24];
u1(pi/4) q[21];
cx q[24],q[21];
u1(-pi/4) q[21];
u1(pi/4) q[24];
cx q[22],q[21];
u1(pi/4) q[25];
u1(pi/4) q[26];
cx q[27],q[25];
cx q[26],q[27];
u1(-pi/4) q[25];
u1(-pi/4) q[27];
cx q[26],q[25];
cx q[26],q[27];
u1(pi/4) q[25];
cx q[27],q[25];
u1(-pi/4) q[25];
u1(pi/4) q[27];
cx q[26],q[25];
u1(pi/4) q[28];
u1(pi/4) q[29];
cx q[31],q[28];
cx q[29],q[31];
u1(-pi/4) q[28];
u1(-pi/4) q[31];
cx q[29],q[28];
cx q[29],q[31];
u1(pi/4) q[28];
cx q[31],q[28];
u1(-pi/4) q[28];
u1(pi/4) q[31];
cx q[29],q[28];
u1(pi/4) q[32];
u1(pi/4) q[33];
cx q[34],q[32];
cx q[33],q[34];
u1(-pi/4) q[32];
u1(-pi/4) q[34];
cx q[33],q[32];
cx q[33],q[34];
u1(pi/4) q[32];
cx q[34],q[32];
u1(-pi/4) q[32];
u1(pi/4) q[34];
cx q[33],q[32];
cx q[3],q[4];
cx q[6],q[7];
cx q[10],q[11];
cx q[13],q[14];
cx q[17],q[18];
cx q[21],q[22];
cx q[25],q[26];
cx q[28],q[29];
cx q[32],q[33];
u1(pi/4) q[7];
u1(pi/4) q[11];
cx q[8],q[7];
cx q[11],q[8];
u1(-pi/4) q[7];
u1(-pi/4) q[8];
cx q[11],q[7];
cx q[11],q[8];
u1(pi/4) q[7];
cx q[8],q[7];
u1(-pi/4) q[7];
u1(pi/4) q[8];
cx q[11],q[7];
u1(pi/4) q[14];
u1(pi/4) q[18];
cx q[15],q[14];
cx q[18],q[15];
u1(-pi/4) q[14];
u1(-pi/4) q[15];
cx q[18],q[14];
cx q[18],q[15];
u1(pi/4) q[14];
cx q[15],q[14];
u1(-pi/4) q[14];
u1(pi/4) q[15];
cx q[18],q[14];
u1(pi/4) q[22];
u1(pi/4) q[26];
cx q[23],q[22];
cx q[26],q[23];
u1(-pi/4) q[22];
u1(-pi/4) q[23];
cx q[26],q[22];
cx q[26],q[23];
u1(pi/4) q[22];
cx q[23],q[22];
u1(-pi/4) q[22];
u1(pi/4) q[23];
cx q[26],q[22];
u1(pi/4) q[29];
u1(pi/4) q[33];
cx q[30],q[29];
cx q[33],q[30];
u1(-pi/4) q[29];
u1(-pi/4) q[30];
cx q[33],q[29];
cx q[33],q[30];
u1(pi/4) q[29];
cx q[30],q[29];
u1(-pi/4) q[29];
u1(pi/4) q[30];
cx q[33],q[29];
u2(0,pi) q[2];
u2(0,pi) q[8];
u2(0,pi) q[9];
u2(0,pi) q[15];
u2(0,pi) q[16];
u2(0,pi) q[23];
u2(0,pi) q[24];
u2(0,pi) q[30];
u2(0,pi) q[31];
u1(pi/4) q[2];
u1(pi/4) q[4];
cx q[5],q[2];
cx q[4],q[5];
u1(-pi/4) q[2];
u1(-pi/4) q[5];
cx q[4],q[2];
cx q[4],q[5];
u1(pi/4) q[2];
cx q[5],q[2];
u1(-pi/4) q[2];
u1(pi/4) q[5];
cx q[4],q[2];
u1(pi/4) q[9];
u1(pi/4) q[11];
cx q[12],q[9];
cx q[11],q[12];
u1(-pi/4) q[9];
u1(-pi/4) q[12];
cx q[11],q[9];
cx q[11],q[12];
u1(pi/4) q[9];
cx q[12],q[9];
u1(-pi/4) q[9];
u1(pi/4) q[12];
cx q[11],q[9];
u1(pi/4) q[16];
u1(pi/4) q[18];
cx q[20],q[16];
cx q[18],q[20];
u1(-pi/4) q[16];
u1(-pi/4) q[20];
cx q[18],q[16];
cx q[18],q[20];
u1(pi/4) q[16];
cx q[20],q[16];
u1(-pi/4) q[16];
u1(pi/4) q[20];
cx q[18],q[16];
u1(pi/4) q[24];
u1(pi/4) q[26];
cx q[27],q[24];
cx q[26],q[27];
u1(-pi/4) q[24];
u1(-pi/4) q[27];
cx q[26],q[24];
cx q[26],q[27];
u1(pi/4) q[24];
cx q[27],q[24];
u1(-pi/4) q[24];
u1(pi/4) q[27];
cx q[26],q[24];
u1(pi/4) q[31];
u1(pi/4) q[33];
cx q[34],q[31];
cx q[33],q[34];
u1(-pi/4) q[31];
u1(-pi/4) q[34];
cx q[33],q[31];
cx q[33],q[34];
u1(pi/4) q[31];
cx q[34],q[31];
u1(-pi/4) q[31];
u1(pi/4) q[34];
cx q[33],q[31];
u1(pi/4) q[15];
u1(pi/4) q[23];
cx q[19],q[15];
cx q[23],q[19];
u1(-pi/4) q[15];
u1(-pi/4) q[19];
cx q[23],q[15];
cx q[23],q[19];
u1(pi/4) q[15];
cx q[19],q[15];
u1(-pi/4) q[15];
u1(pi/4) q[19];
cx q[23],q[15];
u2(0,pi) q[5];
u2(0,pi) q[19];
u2(0,pi) q[20];
u1(pi/4) q[5];
u1(pi/4) q[8];
cx q[12],q[5];
cx q[8],q[12];
u1(-pi/4) q[5];
u1(-pi/4) q[12];
cx q[8],q[5];
cx q[8],q[12];
u1(pi/4) q[5];
cx q[12],q[5];
u1(-pi/4) q[5];
u1(pi/4) q[12];
cx q[8],q[5];
u1(pi/4) q[20];
u1(pi/4) q[23];
cx q[27],q[20];
cx q[23],q[27];
u1(-pi/4) q[20];
u1(-pi/4) q[27];
cx q[23],q[20];
cx q[23],q[27];
u1(pi/4) q[20];
cx q[27],q[20];
u1(-pi/4) q[20];
u1(pi/4) q[27];
cx q[23],q[20];
u2(0,pi) q[12];
u2(0,pi) q[20];
u1(pi/4) q[12];
u1(pi/4) q[19];
cx q[27],q[12];
cx q[19],q[27];
u1(-pi/4) q[12];
u1(-pi/4) q[27];
cx q[19],q[12];
cx q[19],q[27];
u1(pi/4) q[12];
cx q[27],q[12];
u1(-pi/4) q[12];
u1(pi/4) q[27];
cx q[19],q[12];
u1(pi/4) q[12];
u1(pi/4) q[15];
cx q[20],q[12];
cx q[15],q[20];
u1(-pi/4) q[12];
u1(-pi/4) q[20];
cx q[15],q[12];
cx q[15],q[20];
u1(pi/4) q[12];
cx q[20],q[12];
u1(-pi/4) q[12];
u1(pi/4) q[20];
cx q[15],q[12];
u2(0,pi) q[27];
u2(0,pi) q[20];
u2(0,pi) q[9];
u2(0,pi) q[16];
u2(0,pi) q[24];
u2(0,pi) q[31];
u2(0,pi) q[19];
u1(pi/4) q[5];
u1(pi/4) q[7];
cx q[9],q[5];
cx q[7],q[9];
u1(-pi/4) q[5];
u1(-pi/4) q[9];
cx q[7],q[5];
cx q[7],q[9];
u1(pi/4) q[5];
cx q[9],q[5];
u1(-pi/4) q[5];
u1(pi/4) q[9];
cx q[7],q[5];
u1(pi/4) q[12];
u1(pi/4) q[14];
cx q[16],q[12];
cx q[14],q[16];
u1(-pi/4) q[12];
u1(-pi/4) q[16];
cx q[14],q[12];
cx q[14],q[16];
u1(pi/4) q[12];
cx q[16],q[12];
u1(-pi/4) q[12];
u1(pi/4) q[16];
cx q[14],q[12];
u1(pi/4) q[20];
u1(pi/4) q[22];
cx q[24],q[20];
cx q[22],q[24];
u1(-pi/4) q[20];
u1(-pi/4) q[24];
cx q[22],q[20];
cx q[22],q[24];
u1(pi/4) q[20];
cx q[24],q[20];
u1(-pi/4) q[20];
u1(pi/4) q[24];
cx q[22],q[20];
u1(pi/4) q[27];
u1(pi/4) q[29];
cx q[31],q[27];
cx q[29],q[31];
u1(-pi/4) q[27];
u1(-pi/4) q[31];
cx q[29],q[27];
cx q[29],q[31];
u1(pi/4) q[27];
cx q[31],q[27];
u1(-pi/4) q[27];
u1(pi/4) q[31];
cx q[29],q[27];
u1(pi/4) q[27];
u1(pi/4) q[30];
cx q[34],q[27];
cx q[30],q[34];
u1(-pi/4) q[27];
u1(-pi/4) q[34];
cx q[30],q[27];
cx q[30],q[34];
u1(pi/4) q[27];
cx q[34],q[27];
u1(-pi/4) q[27];
u1(pi/4) q[34];
cx q[30],q[27];
u1(pi/4) q[15];
u1(pi/4) q[23];
cx q[19],q[15];
cx q[23],q[19];
u1(-pi/4) q[15];
u1(-pi/4) q[19];
cx q[23],q[15];
cx q[23],q[19];
u1(pi/4) q[15];
cx q[19],q[15];
u1(-pi/4) q[15];
u1(pi/4) q[19];
cx q[23],q[15];
u2(0,pi) q[9];
u2(0,pi) q[16];
u2(0,pi) q[24];
u2(0,pi) q[31];
u2(0,pi) q[34];
u2(0,pi) q[19];
u2(0,pi) q[8];
u2(0,pi) q[15];
u2(0,pi) q[23];
u2(0,pi) q[30];
u1(pi/4) q[7];
u1(pi/4) q[11];
cx q[8],q[7];
cx q[11],q[8];
u1(-pi/4) q[7];
u1(-pi/4) q[8];
cx q[11],q[7];
cx q[11],q[8];
u1(pi/4) q[7];
cx q[8],q[7];
u1(-pi/4) q[7];
u1(pi/4) q[8];
cx q[11],q[7];
u1(pi/4) q[14];
u1(pi/4) q[18];
cx q[15],q[14];
cx q[18],q[15];
u1(-pi/4) q[14];
u1(-pi/4) q[15];
cx q[18],q[14];
cx q[18],q[15];
u1(pi/4) q[14];
cx q[15],q[14];
u1(-pi/4) q[14];
u1(pi/4) q[15];
cx q[18],q[14];
u1(pi/4) q[22];
u1(pi/4) q[26];
cx q[23],q[22];
cx q[26],q[23];
u1(-pi/4) q[22];
u1(-pi/4) q[23];
cx q[26],q[22];
cx q[26],q[23];
u1(pi/4) q[22];
cx q[23],q[22];
u1(-pi/4) q[22];
u1(pi/4) q[23];
cx q[26],q[22];
u1(pi/4) q[29];
u1(pi/4) q[33];
cx q[30],q[29];
cx q[33],q[30];
u1(-pi/4) q[29];
u1(-pi/4) q[30];
cx q[33],q[29];
cx q[33],q[30];
u1(pi/4) q[29];
cx q[30],q[29];
u1(-pi/4) q[29];
u1(pi/4) q[30];
cx q[33],q[29];
cx q[1],q[35];
cx q[4],q[2];
cx q[7],q[5];
cx q[11],q[9];
cx q[14],q[12];
cx q[18],q[16];
cx q[22],q[20];
cx q[26],q[24];
cx q[29],q[27];
cx q[33],q[30];
cx q[0],q[35];
cx q[3],q[4];
cx q[6],q[7];
cx q[10],q[11];
cx q[13],q[14];
cx q[17],q[18];
cx q[21],q[22];
cx q[25],q[26];
cx q[28],q[29];
cx q[32],q[33];
u2(0,pi) q[8];
u2(0,pi) q[15];
u2(0,pi) q[23];
u2(0,pi) q[30];
