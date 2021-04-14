import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class Location extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  location_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  bay_id: number;

  @property({
    type: 'number',
    required: true,
  })
  container_id: number;

  @property({
    type: 'number',
    required: true,
  })
  shelf_id: number;

  @property({
    type: 'number',
    required: true,
  })
  num_slots: number;

  @property({
    type: 'string',
  })
  comment?: string;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Location>) {
    super(data);
  }
}

export interface LocationRelations {
  // describe navigational properties here
}

export type LocationWithRelations = Location & LocationRelations;
