import {Entity, model, property, hasMany} from '@loopback/repository';
import {Location} from './location.model';

@model({settings: {strict: false}})
export class Shelf extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  shelf_id: number;

  @property({
    type: 'number',
    required: true,
  })
  num_slots: number;

  @hasMany(() => Location)
  locations: Location[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Shelf>) {
    super(data);
  }
}

export interface ShelfRelations {
  // describe navigational properties here
}

export type ShelfWithRelations = Shelf & ShelfRelations;
