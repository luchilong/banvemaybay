from sqlalchemy import Column, Integer, Float, \
    String, ForeignKey, Boolean, Date, Enum, Time
from sqlalchemy.orm import relationship
from saleapp import db
from datetime import datetime
from flask_login import UserMixin
from enum import Enum as UserEnum


class SaleBase(db.Model):
    __abstract__ = True

    MaSB = Column(Integer, primary_key=True, autoincrement=True)
    TenSB = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Sanbay(SaleBase):
    __tablename__ = 'Sân Bay'


class Vitrighe(db.Model):
    __tablename__ = 'Vị Trí Ghế'

    MaVTG = Column(Integer, primary_key=True, autoincrement=True)
    TT = Column(Integer, nullable=False)


class Hangkhach(db.Model):
    __tablename__ = 'Hàng Khách'

    MaHK = Column(Integer, primary_key=True, autoincrement=True)
    Hten = Column(String(50))
    CMND = Column(Integer)
    DT = Column(Integer)


class Lichchuyenbay(db.Model):
    __tablename__ = 'Lịch Chuyến Bay'

    MaCB = Column(Integer, primary_key=True, autoincrement=True)
    MaSBden = Column(Integer, ForeignKey(SaleBase.MaSB), nullable=False)
    Ngaygio = Column(Date)
    TGbay = Column(Time)
    SLgheH1 = Column(Integer, nullable=True)
    SLgheH2 = Column(Integer, nullable=True)
    SLgheE = Column(Integer, nullable=True)
    SLghedat = Column(Integer, nullable=True)


class Chitietlichchuyenbay(db.Model):
    __tablename__ = 'Chi Tiết Lịch Chuyến Bay'

    MaCTLCB = Column(Integer, primary_key=True, autoincrement=True)
    MaCB = Column(Integer, ForeignKey(Lichchuyenbay.MaCB), nullable=False)
    MaSBchunggian = Column(Integer, ForeignKey(Sanbay.MaSB), nullable=False)
    TGstop = Column(Time)
    Ghichu = Column(String(255))


class Bangdongia(db.Model):
    __tablename__ = 'Đơn Giá'

    MaDG = Column(Integer, primary_key=True, autoincrement=True)
    MaSB = Column(Integer, ForeignKey(Sanbay.MaSB), nullable=False)
    Giatien = Column(Float)


class Vechuyenbay(db.Model):
    __tablename__ = 'Vé Chuyến Bay'

    MaVCB = Column(Integer, primary_key=True, nullable=False)
    MaCB = Column(Integer, ForeignKey(Lichchuyenbay.MaCB), nullable=False)
    MaHK = Column(Integer, ForeignKey(Hangkhach.MaHK), nullable=False)
    Hangve = Column(String(50))
    MaDG = Column(Integer, ForeignKey(Bangdongia.MaDG), nullable=False)
    MaVTG = Column(Integer, ForeignKey(Vitrighe.MaVTG), nullable=False)


class Phieudatcho(db.Model):
    __tablename__ = 'Phiếu đặt Chổ'

    MaPDC = Column(Integer, primary_key=True, autoincrement=True)
    MaVCB = Column(Integer, ForeignKey(Vechuyenbay.MaVCB), nullable=False)


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class User(SaleBase, UserMixin):
    __tablename__ = 'user'

    email = Column(String(50))
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    joined_date = Column(Date, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)


if __name__ == '__main__':
    db.create_all()