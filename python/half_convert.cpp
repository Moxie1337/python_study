#include<iostream>

using namespace std;

float float16_to_float32(int16_t src){
    if(sizeof(int16_t) == 2){
        int re = src;
        float f = 0.;
        int sign = (re >> 15) ? (-1) : 1;
        int exp = (re >> 10) & 0x1f;
        int eff = re & 0x3ff;
        float half_max = 65504.;
        float half_min = -65504.;
        if (exp == 0x1f && eff) { //nan
            int tmp = (sign < 0) ? 0xffffffff : 0x7fffffff;
            return *(float *)&tmp;
        } else if (exp == 0x1f) { // inf
            int tmp = (sign > 0) ? 0x7f800000 : 0xff800000;
            return *(float *)&tmp;
        }
        if (exp > 0){
            exp -= 15;
            eff = eff | 0x400; // eff from 0.xxx -> 1.xxx
        } else{
            exp = -14;
        }
        int sft;
        sft = exp - 10;
        if (sft < 0) {
            f = (float)sign * eff / (1 << (-sft));
        } else {
            f = ((float)sign) * (1 << sft) * eff;
        }
        return f;
    } else if (sizeof(int16_t) == 4) {
        return src;
    }
}

int main()
{
    float src;
    int16_t ans;

    ans = 0x7b5e;

    src = float16_to_float32(ans);

    cout << "ans = " << src << endl;

    return 0;
}